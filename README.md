# Tableau Story and Dashboards in Flask

This Flask app embeds your Tableau Public story and dashboards using `iframe` URLs derived from `embade code tablue.txt`.

## Live Demo

- https://india-electricity-analysis-2019-and.vercel.app/

## Collaborators

- GitSKY9795 (Sumeet Kumar Yadav)
- vishalkumar2501 (Vishal Kumar)
- Vishal795-knightrider (Vishal Kashyap)
- Shivam Kumar

## Full Documentation

- See `PROJECT_DOCUMENTATION.md` for detailed project documentation, analysis ideas, and reporting structure.


### Website Snapshots

![Home Page](./snapshots/Screenshot%20from%202026-03-13%2022-39-34.png)
![Website Snapshot 2](./snapshots/Screenshot%20from%202026-03-13%2022-40-06.png)
![Story Page](./snapshots/Screenshot%20from%202026-03-13%2022-40-23.png)
![Website Snapshot 4](./snapshots/Screenshot%20from%202026-03-13%2022-40-31.png)
![Website Snapshot 5](./snapshots/Screenshot%20from%202026-03-13%2022-40-40.png)
![Website Snapshot 6](./snapshots/Screenshot%20from%202026-03-13%2022-40-46.png)
![Dashboards Page](./snapshots/Screenshot%20from%202026-03-13%2022-40-59.png)
![Website Snapshot 8](./snapshots/Screenshot%20from%202026-03-13%2022-41-10.png)
![Website Snapshot 9](./snapshots/Screenshot%20from%202026-03-13%2022-41-23.png)
![Conclusion Page](./snapshots/Screenshot%20from%202026-03-13%2022-41-30.png)

## Included Views
- Story page: `StoryonElectricityConsumptioninIndia`
- Dashboards page: `Dashboard1`, `Dashboard2`, `Dashboard3`
- Conclusion page: text summary and key insights

## Run Locally

1. Open terminal in this project folder.
2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. (Optional) enable password protection:

```bash
export APP_PASSWORD="your-password"
export FLASK_SECRET_KEY="replace-with-a-random-secret"
```

5. Start app:

```bash
python3 app.py
```

If your project path has spaces (like yours), this command always works:

```bash
"path" app.py
```

6. Open in browser:

```text
http://127.0.0.1:5000/
```

## Routes

- `/` home page
- `/story` story page
- `/dashboards` page with all three dashboards
- `/conclusion` summary page

## Deploy on Vercel

This project is already configured for Vercel using `vercel.json`.

1. Install Vercel CLI (one time):

```bash
npm i -g vercel
```

2. Login:

```bash
vercel login
```

3. Deploy from this project folder:

```bash
vercel
```

4. For production deployment:

```bash
vercel --prod
```

5. Add environment variables in Vercel Project Settings if needed:

- `APP_PASSWORD` (optional)
- `FLASK_SECRET_KEY` (recommended)

6. After deploy, open your Vercel URL and test:

- `/`
- `/story`
- `/dashboards`
- `/conclusion`
