<p align="center"><a href="https://twitter.com/Aprender_alemao"><img src="https://cdn.jsdelivr.net/gh/dmhendricks/signature-social-icons/icons/round-flat-filled/50px/twitter.png" alt="Twitter" title="Twitter" width="50"/></a><a href="https://www.facebook.com/estudaralemao/"><img src="https://cdn.jsdelivr.net/gh/dmhendricks/signature-social-icons/icons/round-flat-filled/50px/facebook.png" alt="Facebook" title="Facebook" width="50"/></a><a href="https://www.instagram.com/estudaralemao/"><img src="https://cdn.jsdelivr.net/gh/dmhendricks/signature-social-icons/icons/round-flat-filled/50px/instagram.png" alt="Instagram" title="Instagram" width="50"/></a><a href="https://www.youtube.com/c/wwwqueroestudaralemaocombr"><img src="https://cdn.jsdelivr.net/gh/dmhendricks/signature-social-icons/icons/round-flat-filled/50px/youtube.png" alt="YouTube" title="YouTube" width="50"/></a><a href="https://api.whatsapp.com/send?phone=5511989782756&text=I%20want%20to%20know%20..."><img src="https://cdn.jsdelivr.net/gh/dmhendricks/signature-social-icons/icons/round-flat-filled/50px/whatsapp.png" alt="WhatsApp" title="WhatsApp" width="50"/></a><a href="https://www.queroestudaralemao.com.br"><img src="https://cdn.jsdelivr.net/gh/dmhendricks/signature-social-icons/icons/round-flat-filled/50px/website.png" alt="WWW" title="WWW" width="50"/></a><a href="https://br.pinterest.com/chucrutehans/"><img src="https://cdn.jsdelivr.net/gh/dmhendricks/signature-social-icons/icons/round-flat-filled/50px/pinterest.png" alt="Pinterest" title="Pinterest" width="50"/></a><a href="mailto:aulasparticularesdealemaosp@gmail.com?subject=I%20want%20to%20know%20...%20"><img src="https://cdn.jsdelivr.net/gh/dmhendricks/signature-social-icons/icons/round-flat-filled/50px/mail.png" alt="E-Mail" title="E-Mail" width="50"/>
</a>


<p align="center">
<a href=https://github.com/hansalemaos><img src="https://img.shields.io/badge/author-hansalemaos-black"/></a>
<a href=https://www.queroestudaralemao.com.br><img src="https://img.shields.io/badge/from-queroestudaralemao.com.br-darkgreen"/></a>
<a href=#><img src="https://img.shields.io/badge/for-Windows-black"/></a>
<a href=https://codeload.github.com/liangjingkanji/DrakeTyporaTheme/zip/refs/heads/master><img src="https://img.shields.io/badge/Theme-Drake-black"/></a>
<a href=https://github.com/dmhendricks/signature-social-icons><img src="https://img.shields.io/badge/Social-Icons-darkgreen"/></a>
</p><br><!--  -->

# What can you do with Pd2img?

This package allows you to open image files and convert them to a pandas Dataframe
After you are done with your work, you can save the dataframe as an Image




## how to use it
### Everything you need to know
```
pip install pd2img
```

```
from pd2img import Pd2Img
df = Pd2Img(r"C:\Users\Gamer\Documents\Downloads\WhatsApp Image 2022-04-21 at 5.07.14 PM.jpeg")  # creating an instance
df.to_file_rgb('f:\\testimagefile1.png')  # save the dataframe to an RGB image
df.to_file_rgba('f:\\testimagefile2.png')  # save the dataframe to an RGBA image 
np3 = df.to_numpy_rgb()  # convert the image to an numpy array (RGB, not BGR!)
np4 = df.to_numpy_rgba()  # convert the image to an numpy array (RGBA)

print(df.df)  # printing the dataframe
           y     x  red  green  blue
0          0     0  155    150   144
1          0     1  155    150   144
2          0     2  153    148   142
3          0     3  152    147   141
4          0     4  151    147   138
      ...   ...  ...    ...   ...
1224955  956  1275  189    190   185
1224956  956  1276  189    190   185
1224957  956  1277  189    190   185
1224958  956  1278  189    190   185
1224959  956  1279  189    190   185

#Messing around
df.df.loc[(df.df.red > 130) & (df.df.green > 130) & (df.df.blue > 130), 'red'] = 255
df.df.loc[(df.df.red > 130) & (df.df.green > 130) & (df.df.blue > 130), 'green'] = 255
df.df.loc[(df.df.red > 130) & (df.df.green > 130) & (df.df.blue > 130), 'blue'] = 255

```
