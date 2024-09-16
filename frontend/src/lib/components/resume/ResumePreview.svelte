<script lang="ts">
  import type { Resume } from "$lib/interfaces/resume/Resume";
  export let resume: Resume;
  export let resumeElement: HTMLElement | null;

  export let resumeElementSize: {
    height: number;
    width: number;
  } = {
    height: 0,
    width: 0
  };

  let a4Container: HTMLDivElement | null = null;
  let resizeObserver: ResizeObserver | null = null;

  const handleResize: ResizeObserverCallback = (entries) => {
    if (!resumeElementSize) return;

    for (let entry of entries) {
      resumeElementSize.height = entry.contentRect.height;
      resumeElementSize.width = entry.contentRect.width;
    }
  };

  $: if (a4Container) {
    resizeObserver = new ResizeObserver(handleResize);
    resizeObserver.observe(a4Container);
  }
</script>

<section bind:this={resumeElement} class="origin-top-left">
  {#if resume}
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Lobster+Two:ital,wght@0,400;0,700;1,400;1,700&family=Source+Sans+3:ital,wght@0,200..900;1,200..900&display=swap");

      @page {
        size: A4 portrait;
        margin: 1cm;
      }

      .source-sans-3 {
        font-family: "Source Sans 3", sans-serif;
        font-optical-sizing: auto;
        font-weight: 400;
        font-style: normal;
      }

      .lobster-two-bold-italic {
        font-family: "Lobster Two", sans-serif;
        font-weight: 700;
        font-style: italic;
      }

      .a4-size {
        width: 21cm;
      }
    </style>

    <div class="a4-size source-sans-3 flex flex-col gap-3" bind:this={a4Container}>
      {#if resume.personal_info}
        <div class="flex flex-col gap-2">
          <h1 class="lobster-two-bold-italic text-4xl">{resume.personal_info.full_name}</h1>
          <h2 class="text-3xl font-normal"><i>{resume.personal_info.job_title}</i></h2>
        </div>
      {/if}
      {#if resume.links?.length || resume.personal_info}
        <div>
          <div class="flex gap-3">
            {#if resume.personal_info.email || resume.personal_info.phone_number}
              <span>{resume.personal_info.email}</span>
              <a href={"mailto:" + resume.personal_info.phone_number}>
                {resume.personal_info.phone_number}
              </a>
              <span>{resume.personal_info.address}</span>
            {/if}
            {#each resume.links as link (link.id)}
              <a href={link.url}>{link.title?.slice(0, 15)}</a>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.skills?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Skills</h3>
          <div class="grid grid-cols-4 gap-10">
            {#each resume.skills as skill (skill.id)}
              <div>
                <p><strong>{skill.name}</strong></p>
                <p>{skill.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.languages?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Languages</h3>
          <ul class="flex gap-10">
            {#each resume.languages as language (language.id)}
              <li>
                <p>{language.language} - {language.skill_level}</p>
              </li>
            {/each}
          </ul>
        </div>
      {/if}
      {#if resume.projects?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Projects</h3>
          <div class="flex flex-col gap-5">
            {#each resume.projects as project (project.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-3">
                  <span class="col-span-2">
                    <strong>{project.title} - {project.sub_title}</strong>
                  </span>
                  <span class="justify-self-end">
                    {project.start_date} - {project.end_date}
                  </span>
                </div>
                <p class="whitespace-pre-line">{project.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.professional_exps?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Professional Experiences</h3>
          <div class="flex flex-col gap-5">
            {#each resume.professional_exps as professional_exp (professional_exp.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-3">
                  <span class="col-span-2">
                    <strong>{professional_exp.job_title}</strong>, {professional_exp.employer}, {professional_exp.country}
                  </span>
                  <span class="justify-self-end">
                    {professional_exp.start_date} - {professional_exp.end_date}
                  </span>
                </div>
                <p class="whitespace-pre-line">{professional_exp.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.educations?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Education and Courses</h3>
          <div class="flex flex-col gap-5">
            {#each resume.educations as education (education.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-3">
                  <span class="col-span-2">
                    <strong>{education.degree}</strong>, {education.institution}, {education.country}
                  </span>
                  <span class="justify-self-end">
                    {education.start_date} - {education.end_date}
                  </span>
                </div>
                <p class="whitespace-pre-line">{education.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.awards?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Awards</h3>
          <div class="flex flex-col gap-5">
            {#each resume.awards as award (award.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-3">
                  <span class="col-span-2">
                    <strong>{award.title}</strong>, {award.issuer}
                  </span>
                  <span class="justify-self-end">{award.date}</span>
                </div>
                <p class="whitespace-pre-line">{award.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.certificates?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Certificates</h3>
          <div class="flex flex-col gap-5">
            {#each resume.certificates as certificate (certificate.id)}
              <div class="flex flex-col gap-2">
                <p><strong>{certificate.name}</strong></p>
                <p class="whitespace-pre-line">{certificate.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.courses?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Courses</h3>
          <div class="flex flex-col gap-5">
            {#each resume.courses as course (course.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-3">
                  <span class="col-span-2">
                    <strong>{course.degree}</strong>, {course.institution}, {course.country}
                  </span>
                  <span class="justify-self-end">{course.start_date} - {course.end_date}</span>
                </div>
                <p class="whitespace-pre-line">{course.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.interests?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Interests</h3>
          <div class="flex flex-col gap-5">
            {#each resume.interests as interest (interest.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-3">
                  <strong>{interest.name}</strong>
                </div>
                <p class="whitespace-pre-line">{interest.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.publications?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Publications</h3>
          <div class="flex flex-col gap-5">
            {#each resume.publications as publication (publication.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-3">
                  <span class="col-span-2">
                    <strong>{publication.title}</strong>, {publication.publisher}
                  </span>
                  <span class="justify-self-end">
                    {publication.date}
                  </span>
                </div>
                <p class="whitespace-pre-line">{publication.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.references?.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">References</h3>
          <div class="flex flex-col gap-5">
            {#each resume.references as references (references.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-2">
                  <span>
                    <strong>{references.name}</strong>, {references.job_title}, {references.organization}
                  </span>
                  <span class="justify-self-end">
                    {references.phone} - {references.email}
                  </span>
                </div>
              </div>
            {/each}
          </div>
        </div>
      {/if}
    </div>
  {/if}
</section>
