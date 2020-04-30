## Coding
Think first, think slow. Then talk. Write last, write fast.
List and clarify. Testing, testing, testing! Don't go easy on yourself.
You will have the urge to start coding as soon as you have some sort of way. Hold off that!
Try to break your algorithm REALLY HARD!!
Make sure to run your solution with a couple of examples so that interviewer knows what you want to do!

Source of corner cases:
1. Integer: overflow? negative? 0? Duplicated number?
2. LinkedList: circles, Create a dummy node is helpful
3. String: ASCII char? Only numeric value?
4. When calculate mid-point, always use x + (y-x) / 2. Never use (x+y) / 2
5. Thread safety?

Think and talk
* Brutal force to get started
* Don't use edge cases to affect your algorithm too much. Try to find the intrinsic characteristic of the general cases, then use the edge cases to test your algorithm
* Don't commit to an idea too much, sometimes a problem can be solved in a different way from what seems to be the way at first
* What to do when you got stuck:
1. Brutal force
2. DOn't commit to one algorithm too deep
3. Think the problem from the flip side
4. Reduce the problem. 2D -> 1D
5. Sorting helps
* Tools in the box:
Tricks: Sweep line, 2 pointer (fast & slow, opposite), DP, sliding window, greedy
Data Structure: Stack, Segment Tree, Dequeue, PQ

Pseudo
Check if the solution works for the edge cases in step 2.

Write
Good variable name
Write according to the pseudo.
Leave enough space between lines when coding.

Test
Walk thru your cod, immediately after implementation.
Edge case big and small, randomized test case, thread safe?

## System Design
* Structure your design into 5 parts
1. What are the features, and how much request and storage do we need.
2. What are the APIs
3. High-level architecture
4. Business logic + storage choices and schema
5. Scaling + Stability
* System design requires a **top-down** mindset. **Don't** worry about the detail and edge case!
* Don't panic. System design is not like coding, you can't design for everything. There will definitely be cases that you didn't handle! Don't let them bother you ahead of time!
* Think first, Speak Slowly. Don't give out half-hearted answers prematurely.
* Move fast in feature and API. Leave time for business logic and storage. Talk about **details** in business logic. So that they believe it will work.
* When challenged, don't argue. If they have a point, say "that's a good point" and move on! Don't insist on one solution, you want to **show** pros and cos

## Behavioral
* There are just less than 10 common questions. Definitely prepare ahead of time.
* Bring a watch yourself, you need to control the time.
* Don't be a jerk.

reference: https://leetcode.com/discuss/career/217868/My-notes-for-the-night-before-interview
