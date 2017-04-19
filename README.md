# dpatch

Simplifies the creation of patches for Drupal.org issues.

Given a branch in the format `<d.o issue id>-<description>`, `dpatch` will simplify the creation of patches and interdiffs by generating the patches and naming them in accordance with the patch naming guidelines.
  
# Usage

You must be using the git respository of the module you are wanting to make patches against. For a working example, take a look at [this ticket][https://www.drupal.org/node/2462861].

1. Clone the git version of the module. Ensure you are checking out the branch against which you are wanting to commit:

        git clone --branch 7.x-1.x https://git.drupal.org/project/views_autocomplete_filters.git
    
2. Next, create a new branch that includes the issue ID. If you don't have one, open one. The description is just for your purposes and has no impact on `dpatch`.

        git checkout -b 2462861-contextual_filters
    
3. Now, we can make our code changes. **Don't commit your changes until after you have generated a patch.** Here's how the workflow goes:

   1. Make changes.
   2. Generate patch.
   3. Commit changes to branch.
   4. Go back to step 1.

   The commits after comments are important and are how the interdiffs are generated.
  
4. When you are done, you can simply delete the branch and walk away!

# Options

**--parent** allows you to set override the parent branch which the diff is generated against (defaults to whatever branch the ticket is filed against).

# Known Issues

The API caches it's results and so if you try to re-generate patches the patch numbers might not match what you expect because of that.


