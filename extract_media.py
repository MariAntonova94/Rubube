
import os
import ffmpeg
import logging

def extract_audio_and_frames(video_file, video_dir, audio_dir, frames_dir):
    video_path = os.path.join(video_dir, video_file)
    audio_path = os.path.join(audio_dir, f"{os.path.splitext(video_file)[0]}.wav")
    frames_output_dir = os.path.join(frames_dir, os.path.splitext(video_file)[0])
    
    # Проверяем наличие видеофайла
    if not os.path.exists(video_path):
        logging.error(f"Видео файл не найден: {video_path}")
        raise FileNotFoundError(f"Видео файл {video_path} не найден.")
    
    os.makedirs(frames_output_dir, exist_ok=True)

    # Извлечение аудио
    try:
        ffmpeg.input(video_path).output(audio_path).run()
        logging.info(f"Аудио извлечено: {audio_path}")
    except Exception as e:
        logging.error(f"Ошибка при извлечении аудио: {e}")
        raise

    # Извлечение кадров
    try:
        ffmpeg.input(video_path).output(os.path.join(frames_output_dir, 'frame_%04d.jpg'), r=1).run()
        logging.info(f"Кадры извлечены в директорию: {frames_output_dir}")
    except Exception as e:
        logging.error(f"Ошибка при извлечении кадров: {e}")
        raise

    return audio_path, frames_output_dir
