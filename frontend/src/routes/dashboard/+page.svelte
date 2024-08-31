<script>
const isLoggedIn = false;
</script>
  

 {#if isLoggedIn}
    <h1>User dashboard</h1>
    <a href="/resumes">resumes</a>
{:else}
      <p>You aren't logged in.</p>
      <a href="/login">login</a>
{/if}