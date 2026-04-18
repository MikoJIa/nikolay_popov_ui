def test_desks_count(desks_page):
    desks_page.open_page()
    desks_page.all_desks_on_page()

def test_search_field(desks_page):
    desks_page.open_page()
    desks_page.search_field(7)

def test_sort_by_desks(desks_page):
    desks_page.open_page()
    desks_page.sort_by_desk()