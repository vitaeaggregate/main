<script>
	import Resume from "$lib/components/resume/resume.svelte";
	import { account, isAuthenticated } from "$lib/store";
	import { page } from "$app/stores";
	import { goto } from "$app/navigation";

	$: resumeId = Number($page.params.id);
    $: {
        if(!isAuthenticated) goto("/login/test")
        if(account) loadPage();
    }

    const loadPage = () => {
        
    }
</script>

<section>
	<h1>Update Resume (id: {resumeId})</h1>
	<Resume bind:id={resumeId}></Resume>
</section>
