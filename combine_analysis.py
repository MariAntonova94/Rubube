def combine_analysis(audio_data, video_data):
    combined_result = {
        'transcription': audio_data['transcription'],
        'emotions': video_data['emotions'],
        'key_moments': video_data['key_moments']
    }
    return combined_result
