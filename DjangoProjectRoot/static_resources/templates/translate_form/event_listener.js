import { LanguageSelector } from './language_selector.js';

document.querySelectorAll('.language-button').forEach(btn => {
  btn.addEventListener('click', () => {
    LanguageSelector.selectLanguage(btn.dataset.lang);
  });
});