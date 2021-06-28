from django.template import Library

register = Library()


def render_paginator(context, first_last_amount=2, before_after_amount=4):
    orden = context['orden']
    paginator = context['paginator']
    page_numbers = []

    # Pages before current page
    if orden.number > first_last_amount + before_after_amount:
        for i in range(1, first_last_amount + 1):
            page_numbers.append(i)

        page_numbers.append(None)

        for i in range(orden.number - before_after_amount, orden.number):
            page_numbers.append(i)

    else:
        for i in range(1, orden.number):
            page_numbers.append(i)

    # Current page and pages after current page
    if orden.number + first_last_amount + before_after_amount < paginator.num_pages:
        for i in range(orden.number, orden.number + before_after_amount + 1):
            page_numbers.append(i)

        page_numbers.append(None)

        for i in range(paginator.num_pages - first_last_amount + 1, paginator.num_pages + 1):
            page_numbers.append(i)

    else:
        for i in range(orden.number, paginator.num_pages + 1):
            page_numbers.append(i)

    return {
        'paginator': paginator,
        'orden': orden,
        'page_numbers': page_numbers
    }


register.inclusion_tag('pagination.html', takes_context=True)(render_paginator)
