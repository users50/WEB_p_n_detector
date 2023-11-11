<h1 align="center">Привет, меня зовут <a href="https://github.com/users50" target="_blank">Дмитрий Гричанов</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<h3 align="center">Магистрант Уральского федерального университета имени первого президента России Б. Н. Ельцина (УрФУ), программа: Инженерия машинного обучения</h3>
<h4 align="left">Данное Web-приложение на основе библиотеки <a href="https://streamlit.io/">Streamlit</a> предназначено для определения окраски предложений из текстового файла, разделяя предложения на негативные, позитивные и нейтральные. Оно работает на основе модели классификации текста: <a href="https://huggingface.co/blanchefort/rubert-base-cased-sentiment">rubert-base-cased-sentiment</a>  </h4>
<h5 align="left">Для работы программы запустите файл "WEB_p_n_detector.py" (streamlit run WEB_p_n_detector.py). Загрузите txt файл, нажав на кнопку "Browse files" или перетащите файл в окошко "Drag and drop file here". Предложения в файле должны быть роазднлнны "."</h5>
<h5 align="left">Уязвимое место данной программы заключается в том, что она плохо понимает или не понимает совсем отрицательную частицу "не". Например: Я люблю мир - POSITIVE, я не люблю мир - POSITIVE, я ненавижу мир - NEGATIVE. В первом и втором случае программа делает вывод на основе слова "люблю", но не берет в расчет частицу "не"</h5>

