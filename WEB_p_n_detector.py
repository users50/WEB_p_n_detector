import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Загрузка модели для определения тональности (Blanchefort)
model_name = "blanchefort/rubert-base-cased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
sentiment_analyzer = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

def main():
    st.title("Определение тональности предложений (Blanchefort)")

    # Загрузка текстового файла
    uploaded_file = st.file_uploader(label='Выберите текстовый файл ".txt"  для распознавания', type="txt")
        
    if uploaded_file is not None:
        # Чтение содержимого файла и декодирование в строку
        text = uploaded_file.read().decode("utf-8")
        # Определение тональности предложений
        sentences = text.split('.')
        sentiments = [sentiment_analyzer(sentence)[0]['label'] for sentence in sentences if  sentence]

        # Отображение результатов
        st.header("Результаты:")
        st.subheader("Исходный текст:")
        st.text_area("Текст", text, height=200)

        st.subheader("Тональность предложений:")
        for i, sentiment in enumerate(sentiments):
            st.write(f"Предложение {i+1}: {sentiment}")

if __name__ == "__main__":
    main()

