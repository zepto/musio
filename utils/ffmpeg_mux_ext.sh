ffmpeg -muxers -hide_banner | tail -n +5 | cut -d' ' -f4 | xargs -i{} ffmpeg -hide_banner -h muxer={} | grep 'Common extensions' | cut -d' ' -f7 | tr ',' $'\n' | tr -d '.'
