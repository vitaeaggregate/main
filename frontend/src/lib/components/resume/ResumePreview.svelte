<script lang="ts">
  import AddressIcon from "$lib/icons/AddressIcon.svelte";
import EmailIcon from "$lib/icons/EmailIcon.svelte";
	import PhoneIcon from "$lib/icons/PhoneIcon.svelte";
import type { Resume } from "$lib/interfaces/resume/Resume";
import { slide } from 'svelte/transition';

  export let resume: Resume;
  export let sectionElement: HTMLElement | null;

  let showSkills = false;
  let showLanguages = false;
  let showProjects = false;
  let showProfessionalExp = false;
  let showEducation = false;
	let container;

  function fadeSlide(node, options) {
		const slideTrans = slide(node, options)
		return {
			duration: options.duration,
			css: t => `
				${slideTrans.css(t)}
				opacity: ${t};
			`
		};
	}

</script>

<section bind:this={sectionElement}>
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
    </style>


    <div class="source-sans-3 flex flex-col gap-2">
      <div class="flex flex-col gap-2 bg-white rounded-xl p-4">
        <h1 class="lobster-two-bold-italic text-4xl">{resume.personal_info.full_name}</h1>
        <h2 class="text-3xl font-normal"><i>{resume.personal_info.job_title}</i></h2>
        <div class="flex flex-row"><EmailIcon/><span class="pl-2"> <a href={"mailto:" + resume.personal_info.email}>{resume.personal_info.email}</a></span></div>
        <div class="flex flex-row"><PhoneIcon /><span class="pl-2"> {resume.personal_info.phone_number}</span></div>
        <div class="flex flex-row"><AddressIcon /><span class="pl-2">{resume.personal_info.address}</span></div>
      <div>
        {#if resume.links.length}
          <div class="flex gap-3">
            {#each resume.links as link (link.id)}
              <a href={link.url}>{link.title?.slice(0, 15)}</a>
            {/each}
          </div>      
        {/if}
      </div>
      </div>
      {#if resume.skills.length}
      
        <div bind:this={container} class="flex flex-col gap-3 bg-white rounded-xl p-4">
          <button on:click={() => showSkills = !showSkills }><h3 class="w-fit border-b-2 border-black">Skills</h3></button>
          {#if showSkills}
          <div transition:fadeSlide="{{duration: 300}}" class="grid grid-row-4 gap-10">
            {#each resume.skills as skill (skill.id)}
              <div >
                <p><strong>{skill.name}</strong></p>
                <p>{skill.description}</p>
              </div>
            {/each}
          </div>
          {/if}
        </div>
      {/if}
      {#if resume.languages.length}
        <div bind:this={container} class="flex flex-col gap-3 bg-white rounded-xl p-4">
          <button on:click={() => showLanguages = !showLanguages }><h3 class="w-fit border-b-2 border-black">Languages</h3></button>
          {#if showLanguages}
          <div transition:fadeSlide="{{duration: 300}}">
          <ul class="flex gap-10">
            {#each resume.languages as language (language.id)}
              <li>
                <p>{language.language} - {language.skill_level}</p>
              </li>
            {/each}
          </ul>
        </div>
          {/if}
        </div>
      {/if}
      {#if resume.projects.length}
        <div bind:this={container} class="flex flex-col gap-3 bg-white rounded-xl p-4">
          <button on:click={() => showProjects = !showProjects }><h3 class="w-fit border-b-2 border-black">Projects</h3></button>
          {#if showProjects}
          <div transition:fadeSlide="{{duration: 300}}" class="flex flex-col gap-5">
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
          {/if}
        </div>
      {/if}
      {#if resume.professional_exps.length}
        <div bind:this={container} class="flex flex-col gap-3 bg-white rounded-xl p-4">
          <button on:click={() => showProfessionalExp = !showProfessionalExp }><h3 class="w-fit border-b-2 border-black">Professional Experiences</h3></button>
          {#if showProfessionalExp}
          <div transition:fadeSlide="{{duration: 300}}" class="flex flex-col gap-5">
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
          {/if}
        </div>
      {/if}
      {#if resume.educations.length}
        <div bind:this={container} class="flex flex-col gap-3  bg-white rounded-xl p-4">
          <button on:click={() => showEducation = !showEducation }><h3 class="w-fit border-b-2 border-black">Education and Courses</h3></button>
          {#if showEducation}
          <div class="flex flex-col gap-5">
            {#each resume.educations as education (education.id)}
              <div class="flex flex-col gap-2">
                <div class="grid grid-cols-3">
                  <span class="col-span-2">
                    <strong>{education.degree}</strong>, {education.institution}, {education.country}
                  </span>
                  <span class="justify-self-end">{education.start_date} - {education.end_date}</span
                  >
                </div>
                <p class="whitespace-pre-line">{education.description}</p>
              </div>
            {/each}
          </div>
          {/if}
        </div>
      {/if}
    </div>
  {/if}
</section>
