# import os
# import ffmpeg

# def create_shorts(frames_dir, output_video_path, fps=30):
#     frame_pattern = os.path.join(frames_dir, 'frame_%06d.jpg')

#     try:
#         # Собираем кадры в видео-шортс
#         print(f"Creating video from frames in {frames_dir}...")
#         ffmpeg.input(frame_pattern, framerate=fps).output(output_video_path, vcodec='libx264').run()
#         print(f"Shorts video created: {output_video_path}")
    
#     except ffmpeg.Error as e:
#         print("ffmpeg error occurred while creating shorts:")
#         if e.stdout:
#             print("Standard Output:")
#             print(e.stdout.decode('utf-8'))
#         if e.stderr:
#             print("Standard Error:")
#             print(e.stderr.decode('utf-8'))
#         raise e

# # Пример использования
# if __name__ == "__main__":
#     frames_dir = 'frames/example_video'
#     output_video_path = 'output/example_shorts.mp4'
#     create_shorts(frames_dir, output_video_path)










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
