<script lang="ts">
  import { page } from "$app/stores";
  import { deleteResume, getResumeById, updateResume } from "$lib/api/resume";
  import { account, addToast } from "$lib/store";
  import type { Resume } from "$lib/interfaces/resume/Resume";
  import { goto } from "$app/navigation";
  import Button from "$lib/components/Button.svelte";
  import ResumePreview from "$lib/components/resume/ResumePreview.svelte";
  import ResumeComponent from "$lib/components/resume/Resume.svelte";
  import { onDestroy } from "svelte";
  import Toasts from "$lib/components/Toasts.svelte";
  import PlusIcon from "$lib/icons/PlusIcon.svelte";

  let resume: Resume | null = null;
  let originalResume: string | null = null;
  let isModified = false;

  let resumeElement: HTMLElement | null = null;
  let previewContainer: HTMLDivElement | null = null;
  let a4Container: HTMLDivElement | null = null;
  let resizeObserver: ResizeObserver | null = null;

  // Toasts config
  let message = "One or more fields are incorrect!";
  let type = "error";
  let dismissible = true;
  let timeout = 3000;
  // ---------------

  const loadResume = async () => {
    resume = await getResumeById($page.params.id);
    originalResume = JSON.stringify(resume);
  };

  const handleSaveClick = async () => {
    try {
      if (!$account || !resume) return;
      const updatedResume: Resume = await updateResume(resume);
      resume = updatedResume;
      originalResume = JSON.stringify(resume);
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
    if (!originalResume) return;
    resume = JSON.parse(originalResume);
  };

  const handleResize: ResizeObserverCallback = (entries) => {
    for (let entry of entries) {
      const width = entry.contentRect.width;

      if (!a4Container || !resumeElement || !previewContainer) return;

      const scale = width / a4Container.clientWidth;

      resumeElement.style.transform = `scale(${scale})`;

      const currentHeight = Math.round(resumeElement.clientHeight * scale);

      if (previewContainer.clientHeight !== currentHeight)
        previewContainer.style.height = currentHeight + "px";
    }
  };

  const handleResumeDelete = () => {
    if (!resume) return;
    deleteResume(resume.id);
    goto("/my/page");
  };

  //TODO: Remove this
  const handleResumeEdit = () => {
    if (!resume) return;
    goto(`/my/resumes/${resume.id}/edit`);
  };

  const handleDownloadPdf = async () => {
    if (!resume || !resumeElement) throw console.log("Resume not loaded.");

    const body = resumeElement.innerHTML;

    const response = await fetch("./resumes", {
      method: "POST",
      headers: {
        "Content-Type": "applications/json"
      },
      body: JSON.stringify({ body })
    });

    if (!response.ok) throw console.log("Fetch error");

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const invisibleLink = document.createElement("a");
    invisibleLink.href = url;
    invisibleLink.download = "resume.pdf";
    invisibleLink.click();
    URL.revokeObjectURL(url);
  };

  onDestroy(() => {
    if (resizeObserver && previewContainer) resizeObserver.unobserve(previewContainer);
  });

  $: if ($account && $page.params.id) loadResume();

  $: if (previewContainer) {
    resizeObserver = new ResizeObserver(handleResize);
    resizeObserver.observe(previewContainer);
  }

  $: isModified = originalResume !== JSON.stringify(resume);
</script>

{#if $account && $page.params.id && resume}
  <Toasts />
  <section>
    <div class="flex gap-3">
      <Button on:click={handleResumeDelete}>Delete</Button>
      <Button on:click={handleDownloadPdf}>Download</Button>
    </div>
    <div class="grid grid-cols-1 gap-10 overflow-hidden">
      <ResumeComponent bind:value={resume}></ResumeComponent>
      {#if isModified}
        <div
          class="fixed bottom-0 right-0 z-10 flex w-full justify-between gap-5 border-2 bg-slate-100 p-2"
        >
          <Button on:click={handleSaveClick} style="add">Save</Button>
          <Button on:click={handleCancelClick} style="cancel">Cancel</Button>
        </div>
      {/if}
      <div class="rounded-lg bg-slate-100 p-5 shadow-lg">
        <div bind:this={previewContainer}>
          <ResumePreview bind:resume bind:resumeElement bind:a4Container></ResumePreview>
        </div>
      </div>
    </div>
  </section>
{/if}
