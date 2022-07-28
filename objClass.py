class object():
    from selenium import webdriver
    url = 'https://www.pokemon.com/us/'
    BtnSearchPockemon = '/html/body/div[3]/div/nav/div[1]'
    btnCookie = '/html/body/div[18]/div[2]/div/div/div[3]/button'

    txtSearch = '//*[@id="site-search-widget-term"]'
    btnSearch2 = '//*[@id="site-search-widget-submit"]'
    listDetail = '/html/body/div[4]/section/div[2]/div[2]/ul/li[1]'
    exploreMore = '/html/body/div[4]/section[5]/div/div[2]/a'
    loadMore = '//*[@id="loadMore"]'
    assertion1 = '/html/body/div[4]/section[1]/div[2]/div'

    driver = webdriver.Firefox(executable_path=r'C:\\Python310\\Lib\\site-packages\\selenium\\webdriver\\firefox\\geckodriver.exe')
