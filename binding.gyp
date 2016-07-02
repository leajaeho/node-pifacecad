{
  "targets": [{
    "target_name": "pifacecad",
    "sources": ["piface.cc"],
    "include_dirs": ["./src/"],
    "link_settings": {
      "libraries": [
        "../lib/libmcp23s17.a",
        "../lib/libpifacecad.a"
      ]
    },
    "cflags": ["-std=c++11"]
  }]
}