# Vitae Aggrigate

The resume is one of the most important aspects of the job search. It's the first impression companies get and often decides whether you get an interview or not. If you've been in the job market recently, you might have noticed that while there are a lot of resources available to create attractive resumes, there aren't a lot of ways to get actual feedback on your resume. 

Enter Vitae Aggrigate! We offer users a chance to get real feedback from other people. 

# Resume Builder Application

A web-based **resume management system** built using **Svelte**, **TypeScript**, and **Tailwind CSS**. This application allows users to create, view, modify, and download resumes in **ATS-compliant PDF** format. PDF generation is handled entirely client-side using **Puppeteer**.

## Features

- **Create & Edit Resumes**: Add, edit, and remove sections such as skills, education, professional experience, and more.
- **Dynamic Component Rendering**: Components like `SkillItem`, `ProfessionalExp`, and `Link` are rendered dynamically based on user input.
- **Client-side PDF Generation**: Generate ATS-compliant PDFs of resumes using **Puppeteer**.
- **Responsive Design**: Ensure that the application and generated PDFs are mobile-friendly.
- **Notifications**: Users receive notifications for comments on resumes.
- **Resume Sharing**: Control the visibility of resumes with the `is_shareable` field.

## Technologies Used

- ![Svelte](https://img.shields.io/badge/svelte-%23f1413d.svg?style=for-the-badge&logo=svelte&logoColor=white)
- **Svelte**: For building reactive user interfaces.
- ![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
- **TypeScript**: For type safety and enhanced development experience.
- ![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
- **Tailwind**: For utility-first CSS styling.
- ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
- **Django**: Backend REST API to handle resume data, comments, and user information.
- **Puppeteer**: For generating PDFs from Svelte components.

## Project Setup

### Prerequisites

Ensure you have the following installed:

- **Node.js** (v22.6.0+)
- **npm** (v10.8.2+)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/resume-builder.git
    cd resume-builder
    ```

2. **Install dependencies**:
    ```bash
    npm install
    ```

3. **Run the application**:
    ```bash
    npm run dev
    ```

    The application will be accessible at `http://localhost:5173`.

## Deployment

For production, build the application:

```bash
npm run build
