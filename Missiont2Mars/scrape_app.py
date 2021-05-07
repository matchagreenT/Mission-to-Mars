{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "unusual-national",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "\n",
      "\n",
      "====== WebDriver manager ======\n",
      "Current google-chrome version is 90.0.4430\n",
      "Get LATEST driver version for 90.0.4430\n",
      "Current google-chrome version is 90.0.4430\n",
      "Get LATEST driver version for 90.0.4430\n",
      "Driver [C:\\Users\\Timot\\.wdm\\drivers\\chromedriver\\win32\\90.0.4430.24\\chromedriver.exe] found in cache\n",
      "Driver [C:\\Users\\Timot\\.wdm\\drivers\\chromedriver\\win32\\90.0.4430.24\\chromedriver.exe] found in cache\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, redirect\n",
    "from flask_pymongo import PyMongo\n",
    "import scraping"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "technical-realtor",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "together-textbook",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Use flask_pymongo to set up mondo connection\n",
    "app.config[\"MONGO_URI\"] = \"mongodb://localhost:27017/mars_app\"\n",
    "mongo = PyMongo(app)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "entertaining-upper",
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route(\"/\")\n",
    "def index():\n",
    "    mars = mongo.db.mars.find_one()\n",
    "    return render_template(\"index.html\", mars=mars)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "mounted-naples",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "@app.route(\"/scrape\")\n",
    "def scrape():\n",
    "   mars = mongo.db.mars\n",
    "   mars_data = scraping.scrape_all()\n",
    "   mars.update({}, mars_data, upsert=True)\n",
    "   return redirect('/', code=302)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "intellectual-sussex",
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "[2021-05-06 20:39:04,227] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-4-4f975f42b1a7>\", line 4, in index\n",
      "    return render_template(\"index.html\", mars=mars)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "[2021-05-06 20:39:04,227] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-4-4f975f42b1a7>\", line 4, in index\n",
      "    return render_template(\"index.html\", mars=mars)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [06/May/2021 20:39:04] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n",
      "127.0.0.1 - - [06/May/2021 20:39:04] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n",
      "[2021-05-06 20:39:12,923] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-4-4f975f42b1a7>\", line 4, in index\n",
      "    return render_template(\"index.html\", mars=mars)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "[2021-05-06 20:39:12,923] ERROR in app: Exception on / [GET]\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 2447, in wsgi_app\n",
      "    response = self.full_dispatch_request()\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1952, in full_dispatch_request\n",
      "    rv = self.handle_user_exception(e)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1821, in handle_user_exception\n",
      "    reraise(exc_type, exc_value, tb)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\_compat.py\", line 39, in reraise\n",
      "    raise value\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1950, in full_dispatch_request\n",
      "    rv = self.dispatch_request()\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\app.py\", line 1936, in dispatch_request\n",
      "    return self.view_functions[rule.endpoint](**req.view_args)\n",
      "  File \"<ipython-input-4-4f975f42b1a7>\", line 4, in index\n",
      "    return render_template(\"index.html\", mars=mars)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 138, in render_template\n",
      "    ctx.app.jinja_env.get_or_select_template(template_name_or_list),\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 930, in get_or_select_template\n",
      "    return self.get_template(template_name_or_list, parent, globals)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 883, in get_template\n",
      "    return self._load_template(name, self.make_globals(globals))\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\environment.py\", line 857, in _load_template\n",
      "    template = self.loader.load(self, name, globals)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\jinja2\\loaders.py\", line 115, in load\n",
      "    source, filename, uptodate = self.get_source(environment, name)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 60, in get_source\n",
      "    return self._get_source_fast(environment, template)\n",
      "  File \"C:\\Users\\Timot\\anaconda3\\envs\\PythonData\\lib\\site-packages\\flask\\templating.py\", line 89, in _get_source_fast\n",
      "    raise TemplateNotFound(template)\n",
      "jinja2.exceptions.TemplateNotFound: index.html\n",
      "127.0.0.1 - - [06/May/2021 20:39:12] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n",
      "127.0.0.1 - - [06/May/2021 20:39:12] \"\u001b[35m\u001b[1mGET / HTTP/1.1\u001b[0m\" 500 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "incoming-better",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "PythonData",
   "language": "python",
   "name": "pythondata"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
