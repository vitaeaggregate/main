<script lang="ts">
  import type { Resume } from "$lib/interfaces/resume/Resume";

  export let resume: Resume;
  export let sectionElement: HTMLElement | null;
</script>

<section bind:this={sectionElement}>
  {#if resume}
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Lobster+Two:ital,wght@0,400;0,700;1,400;1,700&family=Source+Sans+3:ital,wght@0,200..900;1,200..900&display=swap");

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
    </style>
    <div class="source-sans-3 flex flex-col gap-5 p-10">
      <div class="flex flex-col gap-2">
        <h1 class="lobster-two-bold-italic text-4xl">{resume.personal_info.full_name}</h1>
        <h2 class="text-3xl font-normal"><i>{resume.personal_info.job_title}</i></h2>
      </div>
      <div>
        {#if resume.links.length}
          <div class="flex gap-3">
            <a href={"mailto:" + resume.personal_info.email}>{resume.personal_info.email}</a>
            {#each resume.links as link (link.id)}
              <a href={link.url}>{link.title?.slice(0, 15)}</a>
            {/each}
          </div>
        {/if}
        <span>{resume.personal_info.address}</span>
      </div>
      {#if resume.skills.length}
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
      {#if resume.languages.length}
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
      {#if resume.projects.length}
        <div class="flex flex-col gap-3">
          <h3 class="w-fit border-b-2 border-black">Projects</h3>
          <div class="flex flex-col gap-10">
            {#each resume.projects as project (project.id)}
              <div>
                <p><strong>{project.title} - {project.sub_title}</strong></p>
                <p class="whitespace-pre-line">{project.description}</p>
              </div>
            {/each}
          </div>
        </div>
      {/if}
      {#if resume.professional_exps.length}
        <div></div>
      {/if}
    </div>
  {/if}
</section>
