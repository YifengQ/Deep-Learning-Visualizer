from PIL import Image

# RGB Colors to  Find
blackRGB = [0, 0, 0]
whiteRGB = [255, 255, 255]
# RGBA Values to Replace
transparentRGBA = (0, 0, 0, 0)
redRGBA = (255, 0, 0, 255)
blueRGBA = (0, 0, 255, 255)
greenRGBA = (0, 255, 0, 255)
yellowRGBA = (255, 255, 0, 255)
blackRGBA = (0, 0, 0, 255)

class SuperImposeLayers:

    def __init__(self):
        self.foreground = 0
        self.background = 0
        self.data = 0
        self.new_img = 0

    def super_impose_img(self, foreground_path, background_path, name, result):
        """
        Driver Function that opens the images and converts them into matrix data.
        Then will change the foreground based on user needs and paste it onto the background image.
        :param result:
        :param name:
        :param foreground_path: File path for original foreground image
        :param background_path: File path for original background image
        :return: Saves the new file
        """
        self.savepath = "Superimpose Layer Images/" + name + ".PNG"
        self.foreground = Image.open(foreground_path)
        self.foreground = self.foreground.convert("RGBA")
        self.data = self.foreground.getdata()

        self.foreground.putdata(self.foreground_change(self.data, blackRGB, transparentRGBA, whiteRGB, result))

        self.background = Image.open(background_path)
        # Pastes the transparent foreground on top of the background
        self.background.paste(self.foreground, (0, 0), self.foreground)
        self.background.save(self.savepath, "PNG")
        return self.background

    def foreground_change(self, original_data, find, replace, find_label, recolor_label):
        """
        Takes the image data and finds the black background to be replaced.
        If the pixel is black it will change that pixel to be transparent.
        If label color needs to be changed then it will call another function to replace the label
        color with requested color.
        If label color does not need to be change it will just return the new transparent image
        :param original_data: Data that the image was converted to
        :param find: The RGB value of black to compare
        :param replace: The RGBA value to replace black pixel
        :param find_label: 0 if not needed to change, RGB value of white label
        :param recolor_label: RGBA value of what it needs to change to
        :return: the new image that was created
        """
        self.new_img = []
        for RGB in original_data:
            # Checks if Pixel is Equivalent to Black
            if RGB[0] == find[0] and RGB[1] == find[1] and RGB[2] == find[2]:
                # If black change pixel to 100% transparency
                self.new_img.append(replace)
            else:
                self.new_img.append(RGB)

        if find_label != 0:
            return self.change_label_color(self.new_img, find_label, recolor_label)
        else:
            return self.new_img

    def change_label_color(self, image, to_replace, replace):
        """
        If we want to change the color based on TP, TN, FP, and FN,
        Then this will find the white label and replace it with corresponding color
        :param image: Transparent image data from parent
        :param to_replace: white RGB value of the label
        :param replace: RGBA value to recolor the label
        :return: transparent image with recolored label
        """
        self.new_img = []
        for RGB in image:
            # Checks if Pixel is Equivalent to What we want to Change
            if RGB[0] == to_replace[0] and RGB[1] == to_replace[1] and RGB[2] == to_replace[2]:
                # If if is Replace with new Color
                self.new_img.append(replace)
            else:
                self.new_img.append(RGB)

        return self.new_img