from collections import Counter
import heapq


def main(text):
    # Разбить текст на предложения
    sentences = text.split('. ')
    num_sentences = int(len(sentences) * 0.6)
    # Подсчитать частотность слов
    words = [word for sentence in sentences for word in sentence.split()]
    word_frequency = Counter(words)

    # Оценить важность предложений на основе частотности слов
    sentence_scores = {}
    for sentence in sentences:
        for word in sentence.split():
            if word in word_frequency:
                if len(sentence.split()) < 30:  # Учесть только предложения с меньшим числом слов
                    if sentence not in sentence_scores:
                        sentence_scores[sentence] = word_frequency[word]
                    else:
                        sentence_scores[sentence] += word_frequency[word]


    # Выбрать наиболее важные предложения
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

    # Вернуть сокращенный текст
    summary = '. '.join(summary_sentences)
    return summary
