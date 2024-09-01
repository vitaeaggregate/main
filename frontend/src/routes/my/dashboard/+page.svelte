<script>
    import { onMount } from 'svelte';
  
    onMount(async () => {
      const response = await fetch(URL);
      const data: Resume[] = await response.json();
  
      console.log(data);
    });
  </script>


<div class="grid grid-rows-2">
<div class="m-5"><h1>Dashboard</h1></div>
<div class="grid grid-cols-3 gap-4">
<div class="m-5"><h2>User Info</h2></div>
<div class="m-5"><h2>Resume</h2></div>
<div class="m-5"><h2>Community</h2></div>
</div>
</div>