var pifacecad = require('node-pifacecad');
pifacecad.pifacecad_open();
pifacecad.pifacecad_lcd_backlight_on();
pifacecad.pifacecad_lcd_write('hello hell!');
pifacecad.pifacecad_close();