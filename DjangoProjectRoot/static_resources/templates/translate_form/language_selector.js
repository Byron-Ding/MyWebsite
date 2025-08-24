// 需要导出的字典
export const LanguageSelector = {};

LanguageSelector.urlSwitchLanguage = function(url, newLang) {
    // url 转 对象
    const currentUrl = new URL(url);

    // 单纯的pathname切割
    const segments = currentUrl.pathname.split('/');
    // 替换语言
    segments[1] = newLang;
    // 复合
    currentUrl.pathname = segments.join('/');

    // 生成新的URL
    return currentUrl.origin + currentUrl.pathname + currentUrl.search + currentUrl.hash;
}


LanguageSelector.selectLanguage = function(languageCode) {
    // 获取当前URL
    const url = new URL(window.location.href);
    
    // 刷新页面到新的URL
    window.location.href = LanguageSelector.urlSwitchLanguage(url, languageCode);
};
