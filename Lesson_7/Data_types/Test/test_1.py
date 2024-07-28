from Lesson_7.Data_types.Pages.Mainpage import mainpage
from Lesson_7.Data_types.Pages.Datafilders import datafild


def test_assertion(chrome_browser):
    main_page = mainpage(chrome_browser)
    main_page.find_fields()
    main_page.filling_in_the_fields()
    main_page.click_submit_button()

    data_fild = datafild(chrome_browser)
    data_fild.find_fields()
    data_fild.get_class_first_name()
    data_fild.get_class_last_name()
    data_fild.get_class_address()
    data_fild.get_class_phone()
    data_fild.get_class_zip_code()
    data_fild.get_class_city()
    data_fild.get_class_country()
    data_fild.get_class_job_position()
    data_fild.get_class_company()

    assert "success" in data_fild.get_class_first_name()
    assert "success" in data_fild.get_class_last_name()
    assert "success" in data_fild.get_class_address()
    assert "success" in data_fild.get_class_phone()
    assert "danger" in data_fild.get_class_zip_code()
    assert "success" in data_fild.get_class_city()
    assert "success" in data_fild.get_class_country()
    assert "success" in data_fild.get_class_job_position()
    assert "success" in data_fild.get_class_company()
