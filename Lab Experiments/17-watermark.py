import cv2

def add_watermark(main_img_path, watermark_path, output_path, opacity=0.3):
    main_img = cv2.imread(main_img_path)
    watermark = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
    
    h_main, w_main = main_img.shape[:2]
    h_water, w_water = watermark.shape[:2]
    
    new_width = int(w_main * 0.25)
    new_height = int((new_width * h_water) / w_water)
    
    watermark = cv2.resize(watermark, (new_width, new_height))

    x_pos = w_main - new_width - 10
    y_pos = h_main - new_height - 10
    
    overlay = main_img.copy()

    for i in range(new_height):
        for j in range(new_width):
            if i + y_pos < h_main and j + x_pos < w_main:
                if len(watermark.shape) == 3 and watermark.shape[2] == 4:
                    alpha = watermark[i, j, 3] / 255.0
                    overlay[i + y_pos, j + x_pos] = watermark[i, j, :3]
                else:
                    overlay[i + y_pos, j + x_pos] = watermark[i, j]
    
    output = cv2.addWeighted(overlay, opacity, main_img, 1 - opacity, 0)
    
    cv2.imwrite(output_path, output)
    return output

if __name__ == "__main__":
    main_image = "sample.jpg"
    watermark_image = "watermark.png"
    output_image = "output_watermarked.jpg"
    result = add_watermark(main_image, watermark_image, output_image)
    cv2.imshow('Watermarked Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()