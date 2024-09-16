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

  const loadPage = () => {};

  const handleCreateClick = async () => {
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

  const handleCancelClick = () => {
    goto("/my/page");
  };

  $: if ($account) loadPage();
</script>

{#if $account}
  <section>
    <Toasts />
    <div>
      <h1>New Resume</h1>
      <p>Fields marked with (*) are required!</p>
    </div>
    <br />
    <form class="flex flex-col gap-10">
      <Resume bind:value={resume}></Resume>
      <div
        class="fixed bottom-0 right-0 z-10 flex w-full justify-between gap-5 border-2 bg-slate-100 p-2"
      >
        <Button on:click={handleCreateClick} style="add">Save</Button>
        <Button on:click={handleCancelClick} style="cancel">Cancel</Button>
      </div>
    </form>
  </section>
{/if}
