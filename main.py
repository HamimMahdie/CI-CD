
from flask import Flask, jsonify

app = Flask(__name__)
print("PR3")


def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


@app.route('/')
def home():
    return jsonify({"message": "Docker says- Hello, CI/CD with GCP and Flask!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
