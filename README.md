# BrainFANS Hackathon 2024

From the 19th of November to the 12th of December, a hackathon will commence with
the intention of completing as many of the outstanding issues present on the
[BrainFANS](https://github.com/ejh243/BrainFANS/) repository. People will
be split into 2 teams who will compete for a grand prize.

## What you will be measured against

Teams will need to claim issues on BrainFANS by assigning a member of their
team to them. After claiming an issue, the team that claims it must then create a feature 
branch and work on a solution. Once complete they produce a pull request with their solution. 
At this point, the other team will then review the solution. They can either approve it as is, or 
make suggestions for change. The fact that each team are reviewing each others pull requests 
will hopefully result good quality working solutions 
being committed to the repository. An arbiter will be available to ensure fair
play, and overrule overly picky reviews. 

Teams will be awarded points for engaging in good practise and successfully closing issues.  
As issues are not equal in the magnitude of changes and thus time need to solve the score for 
an issue will be proportional to the number of lines changed in the pull
request. Detailed, more thorough pull requests are hence incentivised. 
At the end of the hackathon, the team with the most lines of code committed to
the main branch will win.

## Teams

The teams are as follows:

| Team 1 |Team 2|
|--------|------|
|Bethan  |Alice |
|Luke    |Emma W|
|Philippa|Greg  |
|Sam     |Marina|


## Avoiding gamification (The rules)

I've tried to think of all of the ways I would potentially game the system to
get the highest number of lines changed. Some of them are subjective however,
and would require an arbiter to actually enforce them.

### One
You cannot approve pull requests made by your own team members

### Two
You cannot hold onto an issue for longer than x days before creating a pull
request
  - After generating a 'full' pull request, you can hold onto the issue for as
  long as you want
  - To prevent gamification here, the arbiter can be called on if you think the
  other team is making partial pull requests in order to eat up all of the
  issues.

### Three
You cannot be overly 'nit' heavy in your pull request reviews as a team.
That is to say, you cannot disapprove a pull request based on opinion.
  - Look [here](https://ejh243.github.io/BrainFANS/Developer-information/Code-review/Conducting-a-code-review#what-to-look-for-in-a-code-review)
  for guidance on reviewing

### Four
If a pull request is not actively worked on for w days and requires fixes
(in terms of functionality/design), the other team is allowed to create a pull
request of their own tackling the same issue
  - This ensures that the issues actually get completed (which is the whole point).

### Five
Teams are encouraged to check the other team's pull requests for any foul
play. For example:
  - Adding unnecessary line breaks to add more lines changed to the total
    - Adding line breaks to ensure code/text doesn't go off the screen is fine.
    - Some lines in the documentation currently are >200 characters long, most
    text editors do not wrap text by default, making it harder to read such
    lines. Adding line breaks to ensure that code/text is readable on all
    screens is therefore fine.
    - An industry standard is 80 characters long. If you have line breaks for
    seemingly no reason (when the same code could fit onto an 80 character long
    line) call the arbiter to assess foul play.

### Six

Not sure how to deal with this gamification, so I will need help on it:
  - If a team is reviewing a pull request and finds a bug in it, they could
  choose *not* to let this be known. 
  - Instead, they could approve the pull request then create a new issue (at
  any point in the future) and create a pull request addressing this bug.
  - This would allow the team who were reviewing the initial pull request to
  'steal' some lines changed. 
  - This is mainly bad as teams can go the other way with their reviews and
  be overly sloppy to take advantage of the new issues that are created. This
  is not what we want. We are trying to remove issues from the backlog, not
  purposely create new ones.

### Seven

Do not purposely ignore pull requests from the other team.
  - If no-one on the opposite team reviews the most recent changes on a pull
  request by the end of the hackathon, the lines changed will be added to
  that teams total Harry Potter style.
    - This means, if a pull request is disapproved by the reviewing team
    (but the problems are fixed in later commits), the lines changed will
    still count if the pull request is not re-reviewed before the end of
    the hackathon.
    - You could still game this system though right? You could make commits
    'fixing' the problems of a pull request on the final day (giving the
    other team no time to actually review it). You could take this even
    further by just adding loads of blank lines into these last minute
    commits.
      - To avoid this scenario, maybe we make it so that you can only
      review pull requests for the final few days (and no new commits can
      be made).
      - Hopefully this doesn't cause issues with hanging pull requests
      after the hackathon.

### Eight

Not sure on this one, but do we count any changes to the 'styling' of the
code?
  - I know that if I **really** wanted to make my team win, I would fix all of
  the weird indentation that is in the repository and all of the stylistic
  inconsistencies. Doing this would rack up lots of points quickly as some
  files have weird indentation on the majority of lines.
  - These are fair commits to make as they often make the code much, much more
  readable. Indentation especially is very helpful when reading the nested `if
  else` statements in the codebase.

### Nine

Should non-handwritten code count? For example, #238 changes over 4000 lines
of code. However, I only *wrote* about 300 lines of code for this pull request.
  - I feel like it might be best to use the automated leader board as a general
  indicator of which team is ahead in the competition, but do a manual count at
  the end for cases like this.

### Ten

Any pull requests that revert changes (for example #69) are fair game as
each team will gain the same number of lines changed. This is fine as this has
the same effect as removing the lines changed from the team who made the
original pull request (that is getting reverted)
  - If you revert a pull request that your own team originally produced, then
  these lines changed should indeed nullify each other (that is to say, no
  lines gained over both pull requests)
