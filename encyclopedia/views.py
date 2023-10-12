from django.shortcuts import render, redirect
import markdown
from . import util
import random


def index(request):
    if request.method == "POST":
        entries =  util.list_entries()
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
        "entries": sorted(util.list_entries())
    })

def entry(request, entry):
    markdown_content = util.get_entry(entry)

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
        entries =  util.list_entries()
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title.lower() in [entry.lower() for entry in entries]:
            return render(request, "encyclopedia/title.html")
        else:
            util.save_entry(title, content)
            markdown_content = util.get_entry(title)
            html_content = markdown.markdown(markdown_content)
            form_action = f"/wiki/{title}"
            # return render(request, "encyclopedia/entries.html", {
            #     "entry": ,
            #     "content": html_content
            # })
            return redirect(form_action)
    else:
        return render(request, "encyclopedia/new.html")
    
def edit(request):
    title = request.GET.get('title')
    if request.method == "POST":
        new_title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(new_title, content)
        markdown_content = util.get_entry(title)
        html_content = markdown.markdown(markdown_content)
        return render(request, "encyclopedia/entries.html", {
            "entry": title,
            "content": html_content
        })
    else:
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
    
def random_entry(request):
    entries = util.list_entries()
    if entries:
        random_entry = random.choice(entries)
        return redirect('entry', entry=random_entry)
    else:
        return redirect('index')


