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

- **Svelte**: For building reactive user interfaces.
- **TypeScript**: For type safety and enhanced development experience.
- **Tailwind CSS**: For utility-first CSS styling.
- **Puppeteer**: For generating PDFs from Svelte components.
- **Django**: Backend REST API to handle resume data, comments, and user information.

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

### PDF Generation

To generate PDFs, Puppeteer is used to capture components and save them as PDFs.

**Steps to generate a PDF**:

1. Ensure your page components are styled properly for print rendering.
2. Use Puppeteer to capture the page and save it as a PDF.
3. Example command for running Puppeteer:
    ```bash
    node puppeteer-script.js
    ```

    Customize the `puppeteer-script.js` file for specific settings and optimizations.

## Routes

- **`/resume/new`**: Create a new resume.
- **`/resume/:id`**: View an existing resume by its ID.

## Deployment

For production, build the application:

```bash
npm run build
