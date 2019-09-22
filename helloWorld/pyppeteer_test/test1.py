import asyncio
from pyppeteer import launch


async def main():
    js1 = '''() =>{
        Object.defineProperties(navigator,{
        webdriver:{
            get: () => false
            }
        })
    }'''
    js2 = '''() => {
        alert (
            window.navigator.webdriver
        )
    }'''
    browser = await launch({'headless': False, 'args': ['--no-sandbox'], })
    page = await browser.newPage()
    await page.setUserAgent("Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko")
    await page.goto('http://www.baidu.com/')
    # await asyncio.sleep(100)
    await page.evaluate(js1) # 将webdriver的属性值设为false
    await page.evaluate(js2) # 再次读取 webdriver属性值，输出为false
    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())
