## Dependencies

 * Python3
 * Python3 packages:
   * (optional) TkInter
   * (optional) paho-mqtt

## Included examples

 * `runner_as_fast_as_possible.py` Headless, as-fast-as-possible simulation.
 * `runner_realtime_threaded.py` Headless, real-time simulation.
 * `runner_realtime_eventloop.py` Simple GUI, real-time simulation.

Each of these scripts will run the Statechart model, and make it do a hardcoded number of 'moves' (picking up and dropping off containers). The `MOVES` constant in `common.py` determines the moves to be made.

## Running the examples

Each of the runners accepts a `time_scale` parameter, for instance:
```
  python runner_realtime_threaded.py 2
```
will run the headless real-time example, with time factor 2 (twice as fast as real-time).

## What are these files??

The following files are of interest:

 * `Statechart.ysc` Statechart model - the file you'll edit.
 * `Statechart.sgen` Code generation options (used by Itemis when generating code)
 * `srcgen/statechart.py` Generated code (by Itemis) from the Statechart model
 * `common.py` Instantiates and initializes the Statechart, and the Controller. Shows how to respond to output events (by creating Observers).
 * `lib/` Directory mostly containing the Statechart runtime (needed for execution).
 * `lib/yakindu/rx.py` Some classes from Itemis.
