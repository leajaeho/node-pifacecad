{
  "targets": [{
    "target_name": "pifacecad",
    "sources": ["piface.cc"],
    "include_dirs": ["./src/"],
    "link_settings": {
      "libraries": [
        "../lib/libpifacecad.a",
        "../lib/libmcp23s17.a"
      ]
    },
    "cflags": ["-std=c++11"]
  }]
}