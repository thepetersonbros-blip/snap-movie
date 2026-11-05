Snap Movie
==========
A stop motion app for kids, built as a web app for the iPad.

Live: https://thepetersonbros-blip.github.io/snap-movie/
Push to main = the iPad gets the new version next time it opens.

Put it on the iPad:
  Open the link in Safari, tap Share, then "Add to Home Screen."
  Use it from the Home Screen icon. Movies made in a Safari tab are kept separately.

How it works:
  - Big red button takes a picture. The last picture shows faintly ("ghost") to line up the next one.
  - Orange = undo. Green = play. Tap a small picture to see it big or throw it away.
  - Turtle / cat / rabbit = slow / medium / fast playback (4 / 8 / 12 pictures a second).
  - Blue button on the play screen makes an MP4. "Save to Photos" opens the iPad share sheet.
  - Hold a movie on the home screen to delete it (you must hold the trash for a second).
  - Pictures stay on the iPad (IndexedDB). Nothing is uploaded anywhere.

Test on a PC without a camera:
  python -m http.server 8765   then open http://127.0.0.1:8765/?demo
  (?demo swaps in a fake camera with a moving ball)

Icons: python make_icons.py
