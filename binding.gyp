{
  "targets": [{
    "target_name": "pifacecad",
    "sources": ["piface.cc"],
    "include_dirs": ["./lib/"],
    "link_settings": {
      "libraries": [
        "../libpifacecad.a",
        "-lmcp23s17",
      ]
    },
    "cflags": ["-std=c++11"]
  }]
}
