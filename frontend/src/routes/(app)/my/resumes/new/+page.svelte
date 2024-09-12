<script lang="ts">
  import { goto } from "$app/navigation";
  import { createResume } from "$lib/api/resume";
  import Resume from "$lib/components/resume/Resume.svelte";
  import type { BaseResume } from "$lib/interfaces/resume/Resume";
  import { account } from "$lib/store";
  import { writable } from "svelte/store";
  import Toasts from "$lib/components/Toasts.svelte";
  import { addToast } from "$lib/store";
  import Button from "$lib/components/Button.svelte";

  let message = "Fields marked * are required";
  let type = "error";
  let dismissible = true;
  let timeout = 3000;

  let resume: BaseResume = {
    title: "",
    personal_info: {},
    is_shareable: false,
    awards: [],
    certificates: [],
    courses: [],
    educations: [],
    interests: [],
    languages: [],
    links: [],
    professional_exps: [],
    projects: [],
    publications: [],
    references: [],
    skills: []
  };

  const resumeStore = writable(resume);

  const loadPage = () => {};

  const handleCreate = async () => {
    try {
      if (!$account || !resume) return;
      resume.member = $account.id;
      resume = await createResume(resume);
      if (resume) goto("/my/page");
    } catch {
      addToast({
        message,
        type,
        dismissible,
        timeout
      });
    }
  };

  $: if ($account) loadPage();
</script>

{#if $account}
  <section>
    <Toasts />
    <div>
      <h1>New Resume</h1>
      <p>Fields marked with (*) are required</p>
    </div>

    <form class="flex flex-col gap-10">
      <Resume bind:value={resume}></Resume>
      <Button on:click={handleCreate}>Add Resume</Button>
    </form>
  </section>
{/if}
