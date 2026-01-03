"""
Morning Fanfare for the Children — Fibonacci Gyroscopic Edition
Captain Leif William Sogge

Concept:
- Woodwinds  = treble gyroscope
- Brass      = bass gyroscope
- Percussion = rhythmic stabilizer
- Movement order and motif repetitions guided by Fibonacci sequence.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any


# ---------- Core structures ----------

@dataclass
class Note:
    pitch: str        # e.g. "C4", "B♭2"
    duration: str     # e.g. "whole", "half", "quarter", "eighth"
    dynamic: str = "" # e.g. "pp", "p", "mp", "mf", "f", "ff"


@dataclass
class Motif:
    name: str
    instrument_group: str   # "woodwinds", "brass", "percussion"
    clef: str               # "treble", "bass", or "rhythmic"
    notes: List[Note]
    description: str = ""


@dataclass
class Movement:
    name: str
    tempo_bpm: int
    key_center: str          # e.g. "C minor", "B♭ major", "C major"
    mood: str
    motif_sequence: List[Dict[str, Any]]  # ordered motifs w/ Fibonacci metadata


@dataclass
class Score:
    title: str
    subtitle: str
    ceremonial_tagline: str
    fibonacci_seed: List[int]
    movements: List[Movement]


# ---------- Fibonacci gyroscope ----------

def fibonacci(n: int) -> List[int]:
    """Basic Fibonacci sequence generator for n terms."""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    seq = [1, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq


# ---------- Define base motifs (from your ceremony) ----------

# I. Soft Engines Stirring (Adagio, C minor)
soft_engines_woodwinds = Motif(
    name="soft_engines_woodwinds",
    instrument_group="woodwinds",
    clef="treble",
    description="Gentle three-note motif rising C–E♭–G, waking the ship softly.",
    notes=[
        Note("C4", "half", "p"),
        Note("E♭4", "quarter", "p"),
        Note("G4", "quarter", "p"),
        Note("C5", "whole", "pp"),
        Note("B♭4", "half", "pp"),
        Note("G4", "half", "pp"),
    ],
)

soft_engines_brass = Motif(
    name="soft_engines_brass",
    instrument_group="brass",
    clef="bass",
    description="Long foundation tones C and E♭ in the low register.",
    notes=[
        Note("C2", "whole", "pp"),
        Note("E♭2", "whole", "pp"),
        Note("G2", "half", "p"),
        Note("B♭2", "half", "p"),
        Note("C2", "whole", "p"),
    ],
)

soft_engines_percussion = Motif(
    name="soft_engines_percussion",
    instrument_group="percussion",
    clef="rhythmic",
    description="Suspended cymbal roll, almost pure texture.",
    notes=[
        Note("cymbal_roll", "whole", "pp"),
    ],
)

# II. B-Flat Undercurrent (Dolce, B♭ major shading)
bflat_undercurrent_woodwinds = Motif(
    name="bflat_undercurrent_woodwinds",
    instrument_group="woodwinds",
    clef="treble",
    description="Warm B♭-centered line like sunlight through curtains.",
    notes=[
        Note("B♭4", "quarter", "mp"),
        Note("D5", "quarter", "mp"),
        Note("F5", "half", "mp"),
        Note("A4", "quarter", "p"),
        Note("F4", "quarter", "p"),
        Note("D4", "half", "p"),
        Note("B♭4", "whole", "pp"),
    ],
)

bflat_undercurrent_brass = Motif(
    name="bflat_undercurrent_brass",
    instrument_group="brass",
    clef="bass",
    description="Low B♭ and F pedestal under the woodwinds.",
    notes=[
        Note("B♭2", "whole", "mp"),
        Note("F2", "whole", "mp"),
        Note("B♭1", "half", "p"),
        Note("F2", "half", "p"),
        Note("B♭2", "whole", "pp"),
    ],
)

bflat_undercurrent_percussion = Motif(
    name="bflat_undercurrent_percussion",
    instrument_group="percussion",
    clef="rhythmic",
    description="Soft quarter-note pulse on hand drum or low tom.",
    notes=[
        Note("low_tom", "quarter", "p"),
    ],
)

# III. Captain’s Call (Allegretto, C minor → B♭)
captains_call_woodwinds = Motif(
    name="captains_call_woodwinds",
    instrument_group="woodwinds",
    clef="treble",
    description="Playful G–B♭–C call motif, like you in the doorway.",
    notes=[
        Note("G4", "quarter", "mf"),
        Note("B♭4", "quarter", "mf"),
        Note("C5", "half", "mf"),
        Note("E♭5", "quarter", "mf"),
        Note("D5", "quarter", "mp"),
        Note("C5", "half", "mp"),
    ],
)

captains_call_brass = Motif(
    name="captains_call_brass",
    instrument_group="brass",
    clef="bass",
    description="Horn response G–B♭–C with grounded support.",
    notes=[
        Note("G2", "half", "mf"),
        Note("B♭2", "half", "mf"),
        Note("C3", "whole", "mf"),
        Note("E♭2", "whole", "mp"),
        Note("C2", "whole", "mp"),
    ],
)

captains_call_percussion = Motif(
    name="captains_call_percussion",
    instrument_group="percussion",
    clef="rhythmic",
    description="Snare on 2 & 4 with bass drum whole-note pulse.",
    notes=[
        Note("snare_2_4", "measure_pattern", "mf"),
        Note("bass_drum", "whole", "mp"),
    ],
)

# IV. The Rising (Crescendo, C minor → C major)
rising_woodwinds = Motif(
    name="rising_woodwinds",
    instrument_group="woodwinds",
    clef="treble",
    description="Ascending C–E♭–G–A♭ figure, then brightening.",
    notes=[
        Note("C4", "eighth", "mp"),
        Note("E♭4", "eighth", "mp"),
        Note("G4", "eighth", "mf"),
        Note("A♭4", "eighth", "mf"),
        Note("F5", "half", "mf"),
        Note("E5", "half", "f"),
        Note("C5", "whole", "f"),
    ],
)

rising_brass = Motif(
    name="rising_brass",
    instrument_group="brass",
    clef="bass",
    description="Pedal tones shifting toward bright C major.",
    notes=[
        Note("C2", "whole", "mp"),
        Note("A♭2", "whole", "mp"),
        Note("F2", "half", "mf"),
        Note("E2", "half", "f"),
        Note("C2", "whole", "f"),
    ],
)

rising_percussion = Motif(
    name="rising_percussion",
    instrument_group="percussion",
    clef="rhythmic",
    description="Timpani C→G with cymbal swell into resolution.",
    notes=[
        Note("timpani_C2", "half", "mf"),
        Note("timpani_G2", "half", "mf"),
        Note("cymbal_swell", "whole", "f"),
    ],
)

# V. Final Blessing (Pianissimo, B♭ major)
final_blessing_woodwinds = Motif(
    name="final_blessing_woodwinds",
    instrument_group="woodwinds",
    clef="treble",
    description="Long B♭ tone, like a forehead kiss.",
    notes=[
        Note("B♭4", "whole", "pp"),
        Note("F5", "half", "pp"),
        Note("D5", "half", "pp"),
        Note("B♭4", "whole", "pp"),
    ],
)

final_blessing_brass = Motif(
    name="final_blessing_brass",
    instrument_group="brass",
    clef="bass",
    description="Low B♭ chord fading into silence.",
    notes=[
        Note("B♭2", "whole", "pp"),
        Note("F2", "whole", "pp"),
        Note("B♭1", "whole", "ppp"),
    ],
)

final_blessing_percussion = Motif(
    name="final_blessing_percussion",
    instrument_group="percussion",
    clef="rhythmic",
    description="Single triangle or chime strike on final B♭.",
    notes=[
        Note("triangle_B♭", "whole", "pp"),
    ],
)


# ---------- Assemble movements with Fibonacci sequencing ----------

# We’ll use the first 5 Fibonacci numbers to “weight” how often motifs appear.
fib = fibonacci(5)  # [1, 1, 2, 3, 5]

# For simplicity:
# - Movement I uses fib[0]
# - Movement II uses fib[1]
# - Movement III uses fib[2]
# - Movement IV uses fib[3]
# - Movement V uses fib[4]

movements: List[Movement] = []

# Helper to build motif sequence entries
def motif_block(motif: Motif, repeats: int, fib_index: int) -> Dict[str, Any]:
    return {
        "motif_name": motif.name,
        "instrument_group": motif.instrument_group,
        "clef": motif.clef,
        "repeats": repeats,
        "fibonacci_index": fib_index,
        "fibonacci_value": fib[fib_index],
    }

# Movement I: Soft Engines Stirring
movements.append(Movement(
    name="I. Soft Engines Stirring",
    tempo_bpm=56,
    key_center="C minor",
    mood="Warm, awakening, gentle authority",
    motif_sequence=[
        motif_block(soft_engines_woodwinds, repeats=fib[0], fib_index=0),
        motif_block(soft_engines_brass,     repeats=fib[0], fib_index=0),
        motif_block(soft_engines_percussion, repeats=fib[0], fib_index=0),
    ],
))

# Movement II: B-Flat Undercurrent
movements.append(Movement(
    name="II. The B-Flat Undercurrent",
    tempo_bpm=64,
    key_center="B♭ major (shaded from C minor)",
    mood="Sunlight through curtains",
    motif_sequence=[
        motif_block(bflat_undercurrent_woodwinds, repeats=fib[1], fib_index=1),
        motif_block(bflat_undercurrent_brass,     repeats=fib[1], fib_index=1),
        motif_block(bflat_undercurrent_percussion, repeats=fib[1], fib_index=1),
    ],
))

# Movement III: Captain’s Call
movements.append(Movement(
    name="III. The Captain's Call",
    tempo_bpm=92,
    key_center="C minor → B♭",
    mood="Playful authority, morning mischief",
    motif_sequence=[
        motif_block(captains_call_woodwinds, repeats=fib[2], fib_index=2),
        motif_block(captains_call_brass,     repeats=fib[2], fib_index=2),
        motif_block(captains_call_percussion, repeats=fib[2], fib_index=2),
    ],
))

# Movement IV: The Rising
movements.append(Movement(
    name="IV. The Rising",
    tempo_bpm=100,
    key_center="C minor → C major",
    mood="Stretching awake, stepping into the day",
    motif_sequence=[
        motif_block(rising_woodwinds, repeats=fib[3], fib_index=3),
        motif_block(rising_brass,     repeats=fib[3], fib_index=3),
        motif_block(rising_percussion, repeats=fib[3], fib_index=3),
    ],
))

# Movement V: Final Blessing
movements.append(Movement(
    name="V. Final Blessing",
    tempo_bpm=52,
    key_center="B♭ major",
    mood="Forehead kiss, shield of protection",
    motif_sequence=[
        motif_block(final_blessing_woodwinds, repeats=fib[4], fib_index=4),
        motif_block(final_blessing_brass,     repeats=fib[4], fib_index=4),
        motif_block(final_blessing_percussion, repeats=fib[4], fib_index=4),
    ],
))

score = Score(
    title="Morning Fanfare for the Children",
    subtitle="Gyroscopic Fibonacci Sequence — Hurricane Code Edition",
    ceremonial_tagline="May the power protect them, and may their day rise in harmony.",
    fibonacci_seed=fib,
    movements=movements,
)


# ---------- Export helper ----------

def to_dict() -> Dict[str, Any]:
    """Return the whole score as nested dictionaries for JSON/YAML export."""
    return {
        "title": score.title,
        "subtitle": score.subtitle,
        "ceremonial_tagline": score.ceremonial_tagline,
        "fibonacci_seed": score.fibonacci_seed,
        "movements": [
            {
                "name": m.name,
                "tempo_bpm": m.tempo_bpm,
                "key_center": m.key_center,
                "mood": m.mood,
                "motif_sequence": m.motif_sequence,
            }
            for m in score.movements
        ],
    }


if __name__ == "__main__":
    import json
    print(json.dumps(to_dict(), indent=2, ensure_ascii=False))
