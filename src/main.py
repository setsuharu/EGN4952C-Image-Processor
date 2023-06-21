import os
import processor

def main():
    folderpath = os.getcwd() + '/test-images'
    outpath = os.getcwd() + '/test-images-out'

    helper = processor.helper()
    imagepaths = helper.get_images_in_dir(folderpath)

    for imagepath in imagepaths:
        # Load the image
        image = processor.image_file(imagepath)

        # Process the image        
        flipped_image = processor.flip_image(image, 1)
        scaled_image = processor.scale_image(image, 0.5)
        rotated_image = processor.rotate_image(image, 45)
        noisy_image = processor.add_gaussian_noise(image, mean=0, std_dev=30)
        sharpened_image = processor.sharpen_image(image)

        # Specify file path for new image
        flipped_image_outpath = outpath + '/' + imagepath.split('/')[-1] + '-flipped' + imagepath.split('/')[-1][-4:]
        scaled_image_outpath = outpath + '/' + imagepath.split('/')[-1] + '-scaled' + imagepath.split('/')[-1][-4:]
        rotated_image_outpath = outpath + '/' + imagepath.split('/')[-1] + '-rotated' + imagepath.split('/')[-1][-4:]
        noisy_image_outpath = outpath + '/' + imagepath.split('/')[-1] + '-noisy' + imagepath.split('/')[-1][-4:]
        sharpened_image_outpath = outpath + '/' + imagepath.split('/')[-1] + '-sharpened' + imagepath.split('/')[-1][-4:]

        # Write new image to disk
        flipped_image.write(flipped_image_outpath)
        scaled_image.write(scaled_image_outpath)
        rotated_image.write(rotated_image_outpath)
        noisy_image.write(noisy_image_outpath)
        sharpened_image.write(sharpened_image_outpath)

        

if __name__ == '__main__':
    main()