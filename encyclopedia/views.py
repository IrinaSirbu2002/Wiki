from django.shortcuts import render, redirect
import markdown
from . import util
import random

types = ['Books', 'Movies', 'TV Series']

def index(request):
    if request.method == "POST":
        entries =  util.list_entries(types)
        query = request.POST.get('q')
        if query.lower() in [entry.lower() for entry in entries]:
            return redirect('entry', entry=query)
        else:
            possible = []
            ok = 1
            for entry in entries:
                if query.lower() in entry.lower():
                    possible.append(entry)
                    ok = 0
            if ok == 0:
                return render(request, "encyclopedia/search.html", {
                    "query": query,
                    "entries": possible
                })
            else:
                return render(request, "encyclopedia/entry_not_found.html")
    
    return render(request, "encyclopedia/index.html", {
        # "entries": sorted(util.list_entries())
        "entries": ['Books', 'Movies', 'TV Series']
    })

def type(request, type):
    
    entries = util.list_entries_by_type(type)
    return render(request, "encyclopedia/type.html", {
        # "entries": sorted(util.list_entries())
        'type': type,
        "entries": entries
    })

def new_type(request):
    type = request.GET.get('type')
    if request.method == "POST":
        entries =  util.list_entries(types)
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title.lower() in [entry.lower() for entry in entries]:
            return render(request, "encyclopedia/title.html")
        else:
            util.save_entry(title, content, type)
            markdown_content = util.get_entry(title, types)
            html_content = markdown.markdown(markdown_content)
            form_action = f"/wiki/{title}"
            return redirect(form_action)
    else:
        return render(request, "encyclopedia/new_type.html")

def entry(request, entry):
    markdown_content = util.get_entry(entry, types)

    # Convert Markdown to HTML
    if markdown_content:
        html_content = markdown.markdown(markdown_content)
    else:
        return render(request, "encyclopedia/entry_not_found.html") 

    return render(request, "encyclopedia/entries.html", {
        "entry": entry,
        "content": html_content
    })

def new(request):
    if request.method == "POST":
        entries =  util.list_entries(types)
        title = request.POST.get('title')
        content = request.POST.get('content')
        type = request.POST.get('type')
        if title.lower() in [entry.lower() for entry in entries]:
            return render(request, "encyclopedia/title.html")
        else:
            util.save_entry(title, content, type)
            markdown_content = util.get_entry(title, types)
            html_content = markdown.markdown(markdown_content)
            form_action = f"/wiki/{title}"
            return redirect(form_action)
    else:
        return render(request, "encyclopedia/new.html")
    
def edit(request):
    title = request.GET.get('title')
    if request.method == "POST":
        new_title = request.POST.get('title')
        content = request.POST.get('content')
        type = request.POST.get('type')
        util.save_entry(new_title, content, type)
        markdown_content = util.get_entry(title, types)
        html_content = markdown.markdown(markdown_content)
        return render(request, "encyclopedia/entries.html", {
            "entry": title,
            "content": html_content
        })
    else:
        content = util.get_entry(title, types)
        this_type = ''
        for type in types:
            if title in util.list_entries_by_type(type):
                this_type = type
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            'type': this_type,
            "content": content
        })
    
def random_entry(request):
    entries = util.list_entries(types)
    if entries:
        random_entry = random.choice(entries)
        return redirect('entry', entry=random_entry)
    else:
        return redirect('index')


