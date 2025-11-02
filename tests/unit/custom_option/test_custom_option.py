def test_custom_option(request):

    custom_value = request.config.getoption("--custom-option")
    print(f"Custom option value: {custom_value}")