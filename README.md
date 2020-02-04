## Django Vue Helper

1. Install vue_helper from Pypi:
`pip install django-vue-helper`

2. Add `vue_helper` to `INSTALLED_APPS` in *settings.py*:
```python
INSTALLED_APPS = [
    ...
    'vue_helper'
]
```

3. Set the following parameters in your config:
```
VUE_DEV_MODE = DEBUG
VUE_APP_NAME = 'frontend'
VUE_APP_DIST_DIR_NAME = 'frontend/dist'
VUE_DEV_SERVER_URL = 'http://localhost:8080'
```

4. In your Django project create a new app `frontend`, this is where you will host Vue static assets:
```
python manage.py startapp frontend
```

5. Add `frontend` app to `INSTALLED_APPS` in *settings.py*:
```python
INSTALLED_APPS = [
    ...
    'vue_helper',
    'frontend'
]
```

6. Create (or modify) `base.html` to have a structure similar to:

```html
{% load vue_helper_tags %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  {% vue_preload_styles %}
  {% vue_preload_scripts %}
  {% vue_styles %}
  {% vue_scripts %}
</head>
<body>
  <div id="app">
    <!-- All content here is accessible by Vue app -->
  </div>
</body>
</html>
```

7. Make sure you have *Vue CLI* installed globally in your system, try to run:
```
vue --version
```

If you get an error output, that means you need to install *Vue CLI*, run the following command in terminal:
```
npm install -g @vue/cli
```

8. After installing *Vue CLI* go into `frontend` app directory in your project and run the following command:
```
vue create static_src
```

This will install a basic *vue* project into `frontend/static_src` directory

9. Go into `frontend/static_src`, add a `vue.config.js` file with the following contents:
```javascript
module.exports = {
  outputDir: "../static/frontend/dist",
  runtimeCompiler: true,
  devServer: {
    public: "http://localhost:8080"
  }
};
```

10. Run `npm run serve` and you should see a vue server starting.

11. Restart your Django server.