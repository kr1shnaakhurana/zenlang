"""ZenLang net package - Networking operations"""
import urllib.request
import urllib.parse
import json

def get(url):
    """HTTP GET request"""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")

def post(url, data):
    """HTTP POST request"""
    try:
        if isinstance(data, dict):
            data = json.dumps(data).encode('utf-8')
        elif isinstance(data, str):
            data = data.encode('utf-8')
        
        req = urllib.request.Request(url, data=data, method='POST')
        req.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")

def request(method, url, data=None, headers=None):
    """Generic HTTP request"""
    try:
        if data and isinstance(data, dict):
            data = json.dumps(data).encode('utf-8')
        elif data and isinstance(data, str):
            data = data.encode('utf-8')
        
        req = urllib.request.Request(url, data=data, method=method.upper())
        
        if headers:
            for key, value in headers.items():
                req.add_header(key, value)
        
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")


# ============ Advanced Networking ============

def download(url, filepath):
    """Download file from URL"""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            with open(filepath, 'wb') as f:
                f.write(data)
        return True
    except Exception as e:
        raise RuntimeError(f"Download error: {e}")

def getJSON(url):
    """GET request and parse JSON"""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")

def postJSON(url, data):
    """POST JSON data"""
    try:
        json_data = json.dumps(data).encode('utf-8')
        req = urllib.request.Request(url, data=json_data, method='POST')
        req.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")

def getHeaders(url):
    """Get response headers"""
    try:
        with urllib.request.urlopen(url) as response:
            return dict(response.headers)
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")

def getStatus(url):
    """Get HTTP status code"""
    try:
        with urllib.request.urlopen(url) as response:
            return response.status
    except Exception as e:
        return 0

def isOnline():
    """Check if internet connection is available"""
    try:
        urllib.request.urlopen('https://www.google.com', timeout=2)
        return True
    except:
        return False


# ============ Advanced Networking Features ============

def put(url, data):
    """HTTP PUT request"""
    try:
        if isinstance(data, dict):
            data = json.dumps(data).encode('utf-8')
        elif isinstance(data, str):
            data = data.encode('utf-8')
        
        req = urllib.request.Request(url, data=data, method='PUT')
        req.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")

def delete(url):
    """HTTP DELETE request"""
    try:
        req = urllib.request.Request(url, method='DELETE')
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")

def patch(url, data):
    """HTTP PATCH request"""
    try:
        if isinstance(data, dict):
            data = json.dumps(data).encode('utf-8')
        elif isinstance(data, str):
            data = data.encode('utf-8')
        
        req = urllib.request.Request(url, data=data, method='PATCH')
        req.add_header('Content-Type', 'application/json')
        
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Network error: {e}")

def uploadFile(url, filepath, field_name='file'):
    """Upload file via multipart/form-data"""
    try:
        import mimetypes
        
        with open(filepath, 'rb') as f:
            file_data = f.read()
        
        boundary = '----WebKitFormBoundary' + ''.join([str(i) for i in range(16)])
        content_type = mimetypes.guess_type(filepath)[0] or 'application/octet-stream'
        
        body = (
            f'--{boundary}\r\n'
            f'Content-Disposition: form-data; name="{field_name}"; filename="{os.path.basename(filepath)}"\r\n'
            f'Content-Type: {content_type}\r\n\r\n'
        ).encode('utf-8')
        body += file_data
        body += f'\r\n--{boundary}--\r\n'.encode('utf-8')
        
        req = urllib.request.Request(url, data=body, method='POST')
        req.add_header('Content-Type', f'multipart/form-data; boundary={boundary}')
        
        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Upload error: {e}")

def urlEncode(params):
    """URL encode parameters"""
    return urllib.parse.urlencode(params)

def urlDecode(query_string):
    """URL decode query string"""
    return dict(urllib.parse.parse_qsl(query_string))

def parseURL(url):
    """Parse URL into components"""
    parsed = urllib.parse.urlparse(url)
    return {
        'scheme': parsed.scheme,
        'host': parsed.netloc,
        'path': parsed.path,
        'params': parsed.params,
        'query': parsed.query,
        'fragment': parsed.fragment
    }

def buildURL(base, params):
    """Build URL with query parameters"""
    if params:
        query = urllib.parse.urlencode(params)
        return f"{base}?{query}"
    return base

def ping(host, timeout=2):
    """Ping host to check availability"""
    try:
        url = f"http://{host}" if not host.startswith('http') else host
        req = urllib.request.Request(url, method='HEAD')
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return response.status == 200
    except:
        return False

def fetchWithRetry(url, retries=3, delay=1):
    """Fetch URL with retry logic"""
    import time
    last_error = None
    
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url) as response:
                return response.read().decode('utf-8')
        except Exception as e:
            last_error = e
            if attempt < retries - 1:
                time.sleep(delay)
    
    raise RuntimeError(f"Network error after {retries} attempts: {last_error}")

def getIP():
    """Get public IP address"""
    try:
        with urllib.request.urlopen('https://api.ipify.org?format=json') as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get('ip', '')
    except:
        return ''

def getUserAgent():
    """Get default user agent"""
    return 'ZenLang/1.0'

def setUserAgent(user_agent):
    """Set custom user agent for requests"""
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', user_agent)]
    urllib.request.install_opener(opener)
    return True
