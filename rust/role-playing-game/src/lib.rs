// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        match self.health {
            0 => Some(Player {
                health: 100,
                mana: if self.level >= 10 { Some(100) } else { None },
                ..*self
            }),
            _ => None,
        }
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        match self.mana {
            None if self.health < mana_cost => {
                self.health = 0;
                0
            }
            None => {
                self.health -= mana_cost;
                0
            }
            Some(val) if val < mana_cost => 0,
            Some(val) => {
                self.mana = Some(val - mana_cost);
                mana_cost * 2
            }
        }
    }
}
