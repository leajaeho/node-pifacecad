{
  "targets": [{
    "target_name": "pifacecad",
    "sources": ["piface.cc"],
    "include_dirs": ["./src/"],
    "link_settings": {
      "libraries": [
        "-lmcp23s17",
        "../lib/libpifacecad.a"
      ]
    },
    "cflags": ["-std=c++11"]
  }]
}
