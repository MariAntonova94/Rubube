
import os
import logging
from extract_media import extract_audio_and_frames
from analyze_audio import transcribe_audio
from analyze_video import analyze_visual_features
from combine_analysis import combine_analysis
from create_shorts import create_shorts

# Настройка логирования
logging.basicConfig(level=logging.INFO, filename='process.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Убедитесь, что правильные пути используются
video_dir = r'E:\Python\Puthon\Hakaton\project\videos'  # Замените на ваш путь
audio_dir = r'E:\Python\Puthon\Hakaton\project\audio'   # Замените на ваш путь
output_dir = r'E:\Python\Puthon\Hakaton\project\output' # Замените на ваш путь
frames_dir = r'E:\Python\Puthon\Hakaton\project\frames' # Замените на ваш путь

# Функция проверки и логирования путей
def check_path(path, description):
    if os.path.exists(path):
        logging.info(f"{description}: Путь существует: {path}")
    else:
        logging.error(f"{description}: Путь не найден: {path}")

# Проверка основных путей
check_path(video_dir, "Директория видеофайлов")
check_path(audio_dir, "Директория аудиофайлов")
check_path(output_dir, "Директория выходных файлов")
check_path(frames_dir, "Директория кадров")

# Проверка файлов в директории видео
video_files = os.listdir(video_dir)
for video_file in video_files:
    video_path = os.path.join(video_dir, video_file)
    check_path(video_path, f"Файл видео {video_file}")

def process_video(video_file):
    video_path = os.path.join(video_dir, video_file)

    # Проверяем путь к файлу перед обработкой
    if not os.path.exists(video_path):
        logging.error(f"Видео файл не найден: {video_path}")
        return
    
    logging.info(f"Обработка видеофайла: {video_path}")
    
    # 1. Извлечение аудио и кадров
    try:
        audio_path, frames_output_dir = extract_audio_and_frames(video_file, video_dir, audio_dir, frames_dir)
    except Exception as e:
        logging.error(f"Ошибка при извлечении аудио или кадров для {video_file}: {e}")
        return

    # 2. Распознавание аудио
    try:
        transcription = transcribe_audio(audio_path)
    except Exception as e:
        logging.error(f"Ошибка при распознавании аудио для {video_file}: {e}")
        return

    # 3. Анализ видео
    try:
        visual_features = analyze_visual_features(frames_output_dir)
    except Exception as e:
        logging.error(f"Ошибка при анализе видео для {video_file}: {e}")
        return

    # 4. Комбинирование аудио и видео данных
    try:
        combined_result = combine_analysis(
            {'transcription': transcription},
            {'emotions': visual_features['emotions'], 'key_moments': visual_features['key_moments']}
        )
        logging.info(f"Комбинированные данные для {video_file}: {combined_result}")
    except Exception as e:
        logging.error(f"Ошибка при комбинировании данных для {video_file}: {e}")
        return

    # 5. Создание шортсов
    try:
        create_shorts(video_file, combined_result['key_moments'])
    except Exception as e:
        logging.error(f"Ошибка при создании шортсов для {video_file}: {e}")

# Обработка каждого видео
for video_file in video_files:
    process_video(video_file)
