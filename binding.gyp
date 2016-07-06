{
  "targets": [{
    "target_name": "pifacecad",
    "sources": ["piface.cc"],
    "include_dirs": ["./src/"],
    "link_settings": {
      "libraries": [
        "../lib/libpifacecad.a",
        "-lmcp23s17"
      ]
    },
    "cflags": ["-std=c++11"]
  }]
}