from src.app import create_app


app = application = create_app()
aa
if __name__ == "__main__":
    app.run(debug=True, port=8000)