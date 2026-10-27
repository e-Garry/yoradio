#ifndef MYOPTIONS_H
#define MYOPTIONS_H

#define L10N_LANGUAGE EN
#define DSP_MODEL DSP_SH1106

/* SH1106 I2C */
#define I2C_SDA 8
#define I2C_SCL 9

/* PCM5100A I2S */
#define I2S_DOUT 7
#define I2S_BCLK 5
#define I2S_LRC 6
#define VS1053_CS 255

/* Rotary encoder: left/A, push button, right/B */
#define ENC_BTNL 1
#define ENC_BTNB 2
#define ENC_BTNR 3
#define ENC_INTERNALPULLUP true

#endif
