






import os
import ffmpeg
import logging

# Определение директорий
video_dir = 'E:/Python/Puthon/Hakaton/project/videos'
output_dir = 'E:/Python/Puthon/Hakaton/project/output'

def create_shorts(video_file, key_moments):
    video_path = os.path.join(video_dir, video_file)
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_folder = os.path.join(output_dir, video_name)
    
    # Проверяем директорию для сохранения шортсов
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    logging.info(f"Создаем шортсы для видео: {video_file}")
    
    for idx, moment in enumerate(key_moments):
        start_time = moment['start']
        end_time = moment['end']
        output_file = os.path.join(output_folder, f'short_{idx}.mp4')
        
        # Проверяем перед созданием шортса
        try:
            ffmpeg.input(video_path, ss=start_time, to=end_time).output(output_file).run()
            logging.info(f"Создан шортс: {output_file}")
        except Exception as e:
            logging.error(f"Ошибка при создании шортса {output_file}: {e}")
